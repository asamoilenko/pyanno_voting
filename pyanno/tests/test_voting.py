import unittest
import numpy as np
from numpy.testing import assert_array_equal
from numpy.testing import assert_array_almost_equal

from pyanno import voting
from pyanno.voting import MISSING_VALUE as MV


class TestVoting(unittest.TestCase):

    def test_labels_count(self):
        annotations = [
            [1,  2, MV, MV],
            [MV, MV,  3,  3],
            [MV,  1,  3,  1],
            [MV, MV, MV, MV],
        ]
        nclasses = 5
        expected = [0, 3, 1, 3, 0]
        result = voting.labels_count(annotations, nclasses)
        self.assertEqual(result, expected)

    def test_majority_vote(self):
        annotations = [
            [1, 2, 2, MV],
            [2, 2, 2, 2],
            [1, 1, 3, 3],
            [1, 3, 3, 2],
            [MV, 2, 3, 1],
            [MV, MV, MV, 3],
        ]
        expected = [2, 2, 1, 3, 1, 3]
        result = voting.majority_vote(annotations)
        self.assertEqual(expected, result)

    def test_majority_vote_empty_item(self):
        # Bug: majority vote with row of invalid annotations fails
        annotations = np.array(
            [[1, 2, 3],
             [MV, MV, MV],
             [1, 2, 2]]
        )
        expected = [1, MV, 2]
        result = voting.majority_vote(annotations)
        self.assertEqual(expected, result)

    def test_dummy(self):

        self.assertEqual(1 + 2, 3)
     
    def test_decimal(self):
	self.assertAlmostEqual(1.1 + 2.2, 3.3)

    def test_sumarr(self):
	x=np.array([1, 1])
	y=np.array([2, 2])
	z=np.array([3, 3])
	assert_array_equal(x + y, z)

    def test_label_frequency(self):
	annotations = [[1, 1, 2], [-1, 1, 2]]
	nclasses = 4
	expected = np.array([ 0. ,  0.6,  0.4,  0. ])
	result = voting.labels_frequency(annotations, nclasses)

	assert_array_almost_equal(expected, result, 2)
	
    def test_label_count_exception_allmissing(self):
	with self.assertRaises(voting.PyannoValueError):
            annotations = np.zeros((2,3)) + MV
            nclasses = 4
            voting.labels_count(annotations, nclasses)

    def test_label_count_exception_emptyan(self):
	with self.assertRaises(voting.PyannoValueError):
 	    annotations = []
	    nclasses = 4
	    voting.labels_count(annotations, nclasses)

    def test_labels_count_newmv(self):
	mv = -999
        annotations = [
            [1,  2, mv, mv],
            [mv, mv,  3,  3],
            [mv,  1,  3,  1],
            [mv, mv, mv, mv],
        ]
        nclasses = 5
        expected = [0, 3, 1, 3, 0]
        result = voting.labels_count(annotations, nclasses, missing_value=mv)
        self.assertEqual(result, expected)

    def test_majority_vote_newmv(self):
        mv = -999
        annotations = [
            [1, 2, 2, mv],
            [2, 2, 2, 2],
            [1, 1, 3, 3],
            [1, 3, 3, 2],
            [mv, 2, 3, 1],
            [mv, mv, mv, 3],
        ]
        expected = [2, 2, 1, 3, 1, 3]
        result = voting.majority_vote(annotations, missing_value=mv)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
