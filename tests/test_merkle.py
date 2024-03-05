from geodefi.utils.merkle import StandartMerkleTree
from geodefi import Geode
from dotenv import dotenv_values
import sys
import os
import pytest
import inspect
from eth_abi import encode

sys.path.append(os.getcwd())


env = dotenv_values(".env")

#################################################
####### StandartMerkleTree ######################
#################################################


def test_tree_initilize():

    tree = StandartMerkleTree()

    assert tree._tree == []
    assert tree._generated == False
    assert tree._depth == 0
    assert tree._numberOfNodes == 0
    assert tree._sizeOfTree == 0
    assert tree._sort == True


@pytest.mark.parametrize(
    "leaves, depht, numberOfNodes, sizeOfTree",
    [
        ([[0]], 1, 1, 2),
        ([[i] for i in range(16)], 5, 16, 32),
        ([[i] for i in range(31)], 6, 31, 64),
        ([[i] for i in range(157)], 9, 157, 512),
    ],
)
def test_tree_generate(leaves, depht, numberOfNodes, sizeOfTree):

    standartMerkleTree = StandartMerkleTree()

    types = ["int"]

    standartMerkleTree.of(leaves, types)

    # standart merkle tree

    assert standartMerkleTree._generated == True
    assert standartMerkleTree._sort == True

    # tests
    assert standartMerkleTree._depth == depht
    assert standartMerkleTree._numberOfNodes == numberOfNodes
    assert standartMerkleTree._sizeOfTree == sizeOfTree


@pytest.mark.parametrize(
    "leaves, types, root",
    [
        # Test case 1: Integer leaves and root
        (
            [[0]],
            ["int"],
            "510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9",
        ),
        (
            [[i] for i in range(16)],
            ["int"],
            "c6b70ea22c9cb271ba84ea37f14787964259e6960b35ae8ddf51f9bd0e3176a3",
        ),
        (
            [[i] for i in range(31)],
            ["int"],
            "aef0f48d8105f948f9c4c44648fb729659fab531b4cb4a3fe3945a22b5f2e2ee",
        ),
        (
            [[i] for i in range(157)],
            ["int"],
            "a0ec4dd2ba6eb5e1578efd8516284a99d17aa87e70d9e36b8afe4a70d2046b4d",
        ),
        # Test case 2: Bytes leaves and root
        (
            [[b"hello"]],
            ["bytes"],
            "1df03627ad4486d6e8e7be19998ae6e769a905b90c5cfc2519dfe035ab543584",
        ),
        (
            [[b"hello"], [b"world"]],
            ["bytes"],
            "7c8b7867dc71b310336f859cc3d8aa46fc1bb5cfec6b95d0097efa0eb6d32bfc",
        ),
        (
            [[b"test", b"merkle", b"tree"]],
            ["bytes", "bytes", "bytes"],
            "f68251b4a7d6d99ef3b8b9f16f1ade23dc084ad7b8f69e9c491cd018e978c169",
        ),
        # Test case 3: Mix of different types and root
        (
            [
                [
                    1,
                    "0xd3cda913deb6f67967b99d67acdfa1712c293601",
                    b"bytesdata",
                    True,
                ]
            ],
            ["int", "address", "bytes", "bool"],
            "97c424a58930c023d603a0912b6a5a385c3203600e6416a7fcfc5c1ce63b1bf0",
        ),
        (
            [
                [
                    i,
                    f"0xd3cda913deb6f67967b99d67acdfa1712c29360{i}",
                    b"bytesdata" + bytes([i]),
                    bool(i % 2 == 0),
                ]
                for i in range(5)
            ],
            ["int", "address", "bytes", "bool"],
            "328e990b1d6f83dfdb9bbced33fdd8d9e02a2e492d9e04989a0a9a6e758ef593",
        ),
        # Test case 4: Only boolean leaves and root
        (
            [[True]],
            ["bool"],
            "b5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22",
        ),
        (
            [[False, True]],
            ["bool", "bool"],
            "0eb5be412f275a18f6e4d622aee4ff40b21467c926224771b782d4c095d1444b",
        ),
        # Test case 5: Only address leaves and root
        (
            [["0xd3cda913deb6f67967b99d67acdfa1712c293601"]],
            ["address"],
            "0c4f91a58661ab3c69dbe0fe58d1ecea2598699df92381a8681760559123de27",
        ),
        # Test case 6: Mix of integers and bytes and root
        (
            [[1, "0xd3cda913deb6f67967b99d67acdfa1712c293601", b"helloworld"]],
            ["int", "address", "bytes"],
            "5afcd76f065f5e4a55528ac105a6c99bcc81467f99d896185e6cafecac5c2dd1",
        ),
        # Test case 7: Only bytes leaves and root
        (
            [[b"bytesdata"]],
            ["bytes"],
            "818c0af0faad90afaffdbc728e419c819e7b9b3f2ce508a92d778739a82712c6",
        ),
        # Test case 8: Mix of integers and booleans and root
        (
            [[1, False], [42, True]],
            ["int", "bool"],
            "29121ab9e52f223f2f465405ba61deb61bf14d96a96c048dda8d1b117ea89c04",
        ),
        # Test case 9: Mix of bytes and booleans and root
        (
            [[b"hello", True], [b"world", False]],
            ["bytes", "bool"],
            "db6cebb0ef6e70da569bb9b581f4044e143345e2e17f4afe069b334d3c3b87ab",
        ),
        # Test case 10: All data types combined and root
        (
            [
                [
                    i,
                    f"0xd3cda913deb6f67967b99d67acdfa1712c29360{i%10}",
                    b"bytesdata" + bytes(i),
                    bool(i % 2),
                ]
                for i in range(123)
            ],
            ["uint256", "address", "bytes", "bool"],
            "20b98c773d1f6a25963777358400ac38e0f63406b8e6e6d078fca9c4a9920853",
        ),
    ],
)
def test_root_merkle_tree(leaves, types, root):
    standartMerkleTree = StandartMerkleTree()

    standartMerkleTree.of(leaves, types)

    assert standartMerkleTree.root == root


def test_new_tree():

    standartMerkleTree = StandartMerkleTree()

    leaves = [[0], [1], [2], [3], [4]]
    types = ["int"]

    tree = standartMerkleTree.of(leaves, types)

    assert tree._tree == [
        None,
        "2c2ba3fc1b5a2d1d6bb3d96aea9c1eeb5ebab4a4fecd3278dd0c9eb098ce9862",
        "e97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162",
        "c167b0e3c82238f4f2d1a50a8b3a44f96311d77b148c30dc0ef863e1a060dcb6",
        "a3c45fa76377c0a96e373793e9023fb2a2d6970e0989ca39ce9f50d9acf834c9",
        "673620737675e2755ce8269a99904022d15da8d5843f5aec205cd243ff80240a",
        "c167b0e3c82238f4f2d1a50a8b3a44f96311d77b148c30dc0ef863e1a060dcb6",
        None,
        "510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9",
        "b5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22",
        "1ab0c6948a275349ae45a06aad66a8bd65ac18074615d53676c09b67809099e0",
        "2584db4a68aa8b172f70bc04e2e74541617c003374de6eb4b295e823e5beab01",
        "c167b0e3c82238f4f2d1a50a8b3a44f96311d77b148c30dc0ef863e1a060dcb6",
        None,
        None,
        None,
    ]
    assert tree._format == "standard-v1"
    assert (
        tree._root
        == "2c2ba3fc1b5a2d1d6bb3d96aea9c1eeb5ebab4a4fecd3278dd0c9eb098ce9862"
    )

    assert (
        tree.root
        == "0x2c2ba3fc1b5a2d1d6bb3d96aea9c1eeb5ebab4a4fecd3278dd0c9eb098ce9862"
    )

    assert tree._tree == standartMerkleTree._tree


def test_get_proofs():

    standartMerkleTree = StandartMerkleTree()

    leaves = [[0], [1], [2], [3], [4]]
    types = ["int"]

    standartMerkleTree.of(leaves, types)

    leaf_hash1 = standartMerkleTree.leafToHash(leaf=[0], types=["int"])
    leaf_hash2 = standartMerkleTree.leafToHash(leaf=[1], types=["int"])
    leaf_hash3 = standartMerkleTree.leafToHash(leaf=[2], types=["int"])
    leaf_hash4 = standartMerkleTree.leafToHash(leaf=[3], types=["int"])

    assert (
        leaf_hash1
        == "510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9"
    )
    assert (
        leaf_hash2
        == "b5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22"
    )
    assert (
        leaf_hash3
        == "1ab0c6948a275349ae45a06aad66a8bd65ac18074615d53676c09b67809099e0"
    )
    assert (
        leaf_hash4
        == "2584db4a68aa8b172f70bc04e2e74541617c003374de6eb4b295e823e5beab01"
    )

    assert standartMerkleTree.getProofs(leaf=leaf_hash1) == [
        "0xb5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22",
        "0x673620737675e2755ce8269a99904022d15da8d5843f5aec205cd243ff80240a",
        "0xc167b0e3c82238f4f2d1a50a8b3a44f96311d77b148c30dc0ef863e1a060dcb6",
    ]
    assert standartMerkleTree.getProofs(leaf=leaf_hash2) == [
        "0x510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9",
        "0xc167b0e3c82238f4f2d1a50a8b3a44f96311d77b148c30dc0ef863e1a060dcb6",
        "0x2c2ba3fc1b5a2d1d6bb3d96aea9c1eeb5ebab4a4fecd3278dd0c9eb098ce9862",
    ]
    assert standartMerkleTree.getProofs(leaf=leaf_hash3) == [
        "0x2584db4a68aa8b172f70bc04e2e74541617c003374de6eb4b295e823e5beab01",
        "0xc167b0e3c82238f4f2d1a50a8b3a44f96311d77b148c30dc0ef863e1a060dcb6",
        "0xc167b0e3c82238f4f2d1a50a8b3a44f96311d77b148c30dc0ef863e1a060dcb6",
    ]
    assert standartMerkleTree.getProofs(leaf=leaf_hash4) == [
        "0x1ab0c6948a275349ae45a06aad66a8bd65ac18074615d53676c09b67809099e0",
        "0xa3c45fa76377c0a96e373793e9023fb2a2d6970e0989ca39ce9f50d9acf834c9",
        "0x2c2ba3fc1b5a2d1d6bb3d96aea9c1eeb5ebab4a4fecd3278dd0c9eb098ce9862",
    ]


def test_invalid_get_proofs():

    standartMerkleTree = StandartMerkleTree()

    leaves = [[0], [1], [2], [3], [4]]
    types = ["int"]

    standartMerkleTree.of(leaves, types)

    with pytest.raises(Exception) as exc_info:
        standartMerkleTree.getProofs(leaf="some_leaf")

    assert str(exc_info.value) == "some_leaf is not a leaf"


def test_properties():

    standartMerkleTree = StandartMerkleTree()

    leaves = [[0], [1], [2], [3]]
    types = ["int"]

    standartMerkleTree.of(leaves, types)

    assert (
        standartMerkleTree.root
        == "e97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162"
    )
    assert standartMerkleTree.generated == True
    assert standartMerkleTree.numberOfNodes == 4
    assert standartMerkleTree.tree == [
        "e97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162",
        "a3c45fa76377c0a96e373793e9023fb2a2d6970e0989ca39ce9f50d9acf834c9",
        "673620737675e2755ce8269a99904022d15da8d5843f5aec205cd243ff80240a",
        "510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9",
        "b5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22",
        "1ab0c6948a275349ae45a06aad66a8bd65ac18074615d53676c09b67809099e0",
        "2584db4a68aa8b172f70bc04e2e74541617c003374de6eb4b295e823e5beab01",
    ]
    assert standartMerkleTree.sizeOfTree == 8
    assert standartMerkleTree.depth == 3

    assert standartMerkleTree.leaves == [
        "510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9",
        "b5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22",
        "1ab0c6948a275349ae45a06aad66a8bd65ac18074615d53676c09b67809099e0",
        "2584db4a68aa8b172f70bc04e2e74541617c003374de6eb4b295e823e5beab01",
    ]


def test_reset_the_tree():

    standartMerkleTree = StandartMerkleTree()

    leaves = [[0], [1], [2], [3]]
    types = ["int"]

    standartMerkleTree.of(leaves, types)

    # Reset
    standartMerkleTree.reset()

    assert standartMerkleTree.root == None
    assert standartMerkleTree.generated == False
    assert standartMerkleTree.numberOfNodes == 0
    assert standartMerkleTree.tree == []
    assert standartMerkleTree.sizeOfTree == 0
    assert standartMerkleTree.depth == 0
    assert standartMerkleTree.leaves == []


def test_generate_with_str_bool():

    standartMerkleTree1 = StandartMerkleTree()
    standartMerkleTree2 = StandartMerkleTree()
    standartMerkleTree3 = StandartMerkleTree()

    types = ["bool"]

    leaves1 = [[True], [False]]
    leaves2 = [["true"], ["false"]]
    leaves3 = [["True"], ["False"]]

    standartMerkleTree1.of(leaves1, types)
    standartMerkleTree2.of(leaves2, types)
    standartMerkleTree3.of(leaves3, types)

    assert (
        standartMerkleTree1.root
        == standartMerkleTree2.root
        == standartMerkleTree3.root
    )


def test_generate_with_str_bytes():

    standartMerkleTree1 = StandartMerkleTree()
    standartMerkleTree2 = StandartMerkleTree()
    standartMerkleTree3 = StandartMerkleTree()

    types = ["bytes"]
    # bytes string like 'aaaaaaaa'
    leaves1 = [
        [b"\xaa\xaa\xaa\xaa"],
        [b"\xbb\xbb\xbb\xbb"],
        [b"\xcc\xcc\xcc\xcc"],
        [b"\xdd\xdd\xdd\xdd"],
        [b"\xee\xee\xee\xee"],
        [b"\xff\xff\xff\xff"],
    ]

    # hex string like '0xaaaaaaaa'
    leaves2 = [[f"0x{i*8}"] for i in ["a", "b", "c", "d", "e", "f"]]

    # string like aaaaaaaa
    leaves3 = [[f"{i*8}"] for i in ["a", "b", "c", "d", "e", "f"]]

    standartMerkleTree1.of(leaves1, types)
    standartMerkleTree2.of(leaves2, types)
    standartMerkleTree3.of(leaves3, types)

    assert (
        standartMerkleTree1.root
        == standartMerkleTree2.root
        == standartMerkleTree3.root
    )


def test_concat():

    result = StandartMerkleTree.concat("0xAAA", "0xBBB")
    assert result == "0xAAABBB"

    result = StandartMerkleTree.concat("0xAAA", "0xBBB", sort=True)
    assert result == "0xAAABBB"

    result = StandartMerkleTree.concat("0xAAA", "0xBBB", sort=False)
    assert result == "0xAAABBB"

    result = StandartMerkleTree.concat("", "")
    assert result == "0x"

    result = StandartMerkleTree.concat("0xAAA", "")
    assert result == "0xAAA"

    result = StandartMerkleTree.concat("123", "456", sort=True)
    assert result == "0x123456"

    result = StandartMerkleTree.concat("aBc", "cBa", sort=True)
    assert result == "0xaBccBa"


def test_invalid_concat():

    with pytest.raises(ValueError, match="concat function works with strings"):
        StandartMerkleTree.concat(123, "0xBBB")

    with pytest.raises(ValueError, match="concat function works with strings"):
        StandartMerkleTree.concat("0xAAA", 456)


def test_print_tree(capsys):

    standartMerkleTree = StandartMerkleTree()

    leaves = [[0], [1], [2], [3]]
    types = ["int"]

    standartMerkleTree.of(leaves, types)

    # Call the function that prints to stdout
    standartMerkleTree.printTree()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check the printed output
    assert (
        captured.out
        == "============== TREE ==============\n1 |  |_: e97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162\n2 |  |  |__: a3c45fa76377c0a96e373793e9023fb2a2d6970e0989ca39ce9f50d9acf834c9\n4 |  |  |  |___: 510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9\n5 |  |  |  |___: b5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22\n3 |  |  |__: 673620737675e2755ce8269a99904022d15da8d5843f5aec205cd243ff80240a\n6 |  |  |  |___: 1ab0c6948a275349ae45a06aad66a8bd65ac18074615d53676c09b67809099e0\n7 |  |  |  |___: 2584db4a68aa8b172f70bc04e2e74541617c003374de6eb4b295e823e5beab01\n"
    )


def test_str():

    standartMerkleTree = StandartMerkleTree()
    leaves = [[0], [1], [2], [3]]
    types = ["int"]

    standartMerkleTree.of(leaves, types)
    # Call the function that prints to stdout

    assert (
        str(standartMerkleTree)
        == "Tree Root Hash: e97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162"
    )

    # Empty-Tree

    standartMerkleTree.reset()

    assert str(standartMerkleTree) == "The tree has no leaves yet."


def test_is_valid_hex_string_raises_value_error():
    tree = StandartMerkleTree()

    with pytest.raises(ValueError, match="is not hex-string."):
        tree.of(values=[["0xInvalid"]], types=["bytes"])

    with pytest.raises(ValueError, match="is not hex-string."):
        tree.of(values=[["0xNotHex"]], types=["bytes"])

    with pytest.raises(ValueError, match="is not hex-string."):
        tree.of(values=[["0x0x0x"]], types=["bytes"])

    with pytest.raises(ValueError, match="is not hex-string."):
        tree.of(values=[["0x12345z"]], types=["bytes"])

    with pytest.raises(ValueError, match="is not hex-string."):
        tree.of(values=[["0z0x"]], types=["bytes"])

    with pytest.raises(ValueError, match="is not hex-string."):
        tree.of(values=[["12345z"]], types=["bytes"])


def test_is_valid_integer():
    tree = StandartMerkleTree()

    with pytest.raises(ValueError, match="is not integer or unsigned integer."):
        tree.of(values=[["abc"]], types=["uint"])

    with pytest.raises(ValueError, match="is not integer or unsigned integer."):
        tree.of(values=[["12.34"]], types=["uint256"])

    with pytest.raises(ValueError, match="is not integer or unsigned integer."):
        tree.of(values=[["0x12"]], types=["int"])

    with pytest.raises(ValueError, match="is not integer or unsigned integer."):
        tree.of(values=[["None"]], types=["uint256"])


def test_is_valid_boolean():
    tree = StandartMerkleTree()

    with pytest.raises(ValueError, match="is not boolean."):
        tree.of(values=[["abc"]], types=["bool"])

    with pytest.raises(ValueError, match="is not boolean."):
        tree.of(values=[["TRUE"]], types=["bool"])

    with pytest.raises(ValueError, match="is not boolean."):
        tree.of(values=[["FALSE"]], types=["bool"])

    with pytest.raises(ValueError, match="is not boolean."):
        tree.of(values=[["None"]], types=["bool"])


def test_check_bytes_invalid():
    tree = StandartMerkleTree()

    with pytest.raises(ValueError, match="is not bytes."):
        tree.of(values=[[[0x01, 0x02, 0x03]]], types=["bytes"])

    with pytest.raises(ValueError, match="is not bytes."):
        tree.of(values=[[123]], types=["bytes32"])

    with pytest.raises(ValueError, match="is not bytes."):
        tree.of(values=[[True]], types=["bytes32"])


#################################################
#################### Tree #######################
#################################################


def test_tree_init():

    standartMerkleTree = StandartMerkleTree()
    leaves = [[0], [1], [2], [3]]
    types = ["int"]

    tree = standartMerkleTree.of(leaves, types)

    assert tree._types == ["int"]
    assert tree._values == [[0], [1], [2], [3]]
    assert tree._format == "standard-v1"
    assert (
        tree._root
        == "e97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162"
    )

    assert tree._tree == [
        None,
        "e97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162",
        "a3c45fa76377c0a96e373793e9023fb2a2d6970e0989ca39ce9f50d9acf834c9",
        "673620737675e2755ce8269a99904022d15da8d5843f5aec205cd243ff80240a",
        "510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9",
        "b5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22",
        "1ab0c6948a275349ae45a06aad66a8bd65ac18074615d53676c09b67809099e0",
        "2584db4a68aa8b172f70bc04e2e74541617c003374de6eb4b295e823e5beab01",
    ]

    assert (
        repr(tree)
        == "MerkleTree(\n\tformat: 'standard-v1',\n\ttree:\n\t  '0xe97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162'\n\t  '0xa3c45fa76377c0a96e373793e9023fb2a2d6970e0989ca39ce9f50d9acf834c9'\n\t  '0x673620737675e2755ce8269a99904022d15da8d5843f5aec205cd243ff80240a'\n\t  '0x510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9'\n\t  '0xb5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22'\n\t  '0x1ab0c6948a275349ae45a06aad66a8bd65ac18074615d53676c09b67809099e0'\n\t  '0x2584db4a68aa8b172f70bc04e2e74541617c003374de6eb4b295e823e5beab01',\n\tvalues:\n\t\t[[0], [1], [2], [3]],\n\troot:\n\t  0xe97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162\n\tleaf_encoding:  ['int'])"
    )


def test_tree_properties():
    standartMerkleTree = StandartMerkleTree()
    leaves = [[0], [1], [2], [3]]
    types = ["int"]

    tree = standartMerkleTree.of(leaves, types)

    assert tree.leaf_encodings == ["int"]
    assert tree.values == [[0], [1], [2], [3]]
    assert tree.format == "standard-v1"
    assert (
        tree.root
        == "0xe97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162"
    )

    assert tree.tree == [
        "e97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162",
        "a3c45fa76377c0a96e373793e9023fb2a2d6970e0989ca39ce9f50d9acf834c9",
        "673620737675e2755ce8269a99904022d15da8d5843f5aec205cd243ff80240a",
        "510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9",
        "b5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22",
        "1ab0c6948a275349ae45a06aad66a8bd65ac18074615d53676c09b67809099e0",
        "2584db4a68aa8b172f70bc04e2e74541617c003374de6eb4b295e823e5beab01",
    ]


def test_tree_hexify():

    standartMerkleTree = StandartMerkleTree()
    leaves = [[0], [1], [2], [3]]
    types = ["int"]

    tree = standartMerkleTree.of(leaves, types)

    assert tree.tree == [
        "e97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162",
        "a3c45fa76377c0a96e373793e9023fb2a2d6970e0989ca39ce9f50d9acf834c9",
        "673620737675e2755ce8269a99904022d15da8d5843f5aec205cd243ff80240a",
        "510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9",
        "b5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22",
        "1ab0c6948a275349ae45a06aad66a8bd65ac18074615d53676c09b67809099e0",
        "2584db4a68aa8b172f70bc04e2e74541617c003374de6eb4b295e823e5beab01",
    ]

    new_tree = tree._tree_hexify(tree.tree)

    assert new_tree == [
        "0xe97e7870ffec941070df3ac0255521c04008ba2c5a2b9ebb33e0d4adee758162",
        "0xa3c45fa76377c0a96e373793e9023fb2a2d6970e0989ca39ce9f50d9acf834c9",
        "0x673620737675e2755ce8269a99904022d15da8d5843f5aec205cd243ff80240a",
        "0x510e4e770828ddbf7f7b00ab00a9f6adaf81c0dc9cc85f1f8249c256942d61d9",
        "0xb5d9d894133a730aa651ef62d26b0ffa846233c74177a591a4a896adfda97d22",
        "0x1ab0c6948a275349ae45a06aad66a8bd65ac18074615d53676c09b67809099e0",
        "0x2584db4a68aa8b172f70bc04e2e74541617c003374de6eb4b295e823e5beab01",
    ]
