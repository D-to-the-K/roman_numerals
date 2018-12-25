#!/usr/bin/env python3

import unittest
from roman_numerals.roman_numerals import RomanNumerals


class TestRomanNumerals(unittest.TestCase):

    def test_import_ok(self):
        RomanNumerals()

    def test_parse_negative_int_raises_error(self):
        self.assertRaises(ValueError, RomanNumerals.int_to_roman_string, -1)

    def test_parse_negative_int_from_constructor_raises_error(self):
        self.assertRaises(ValueError, RomanNumerals, integer=-1)

    def test_parse_0_raises_error(self):
        self.assertRaises(ValueError, RomanNumerals.int_to_roman_string, 0)

    def test_parse_0_from_constructor_raises_error(self):
        self.assertRaises(ValueError, RomanNumerals, integer=0)

    def test_parse_4000_raises_error(self):
        self.assertRaises(ValueError, RomanNumerals.int_to_roman_string, 4000)

    def test_parse_4000_from_constructor_raises_error(self):
        self.assertRaises(ValueError, RomanNumerals, integer=4000)

    def test_parse_1_is_valid(self):
        rn = RomanNumerals()
        rn.parse_from_int(1)
        self.assertTrue(rn.is_valid)

    def test_parse_1_from_constructor_is_valid(self):
        rn = RomanNumerals(integer=1)
        self.assertTrue(rn.is_valid)

    def test_parse_3999_is_valid(self):
        rn = RomanNumerals()
        rn.parse_from_int(3999)
        self.assertTrue(rn.is_valid)

    def test_parse_3999_from_constructor_is_valid(self):
        rn = RomanNumerals(integer=3999)
        self.assertTrue(rn.is_valid)

    def test_convert_1_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(1), "I")

    def test_convert_2_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(2), "II")

    def test_convert_3_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(3), "III")

    def test_convert_4_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(4), "IV")

    def test_convert_5_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(5), "V")

    def test_convert_6_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(6), "VI")

    def test_convert_7_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(7), "VII")

    def test_convert_8_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(8), "VIII")

    def test_convert_9_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(9), "IX")

    def test_convert_10_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(10), "X")

    def test_convert_20_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(20), "XX")

    def test_convert_21_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(21), "XXI")

    def test_convert_32_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(32), "XXXII")

    def test_convert_43_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(43), "XLIII")

    def test_convert_54_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(54), "LIV")

    def test_convert_65_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(65), "LXV")

    def test_convert_76_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(76), "LXXVI")

    def test_convert_87_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(87), "LXXXVII")

    def test_convert_98_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(98), "XCVIII")

    def test_convert_99_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(99), "XCIX")

    def test_convert_100_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(100), "C")

    def test_convert_200_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(200), "CC")

    def test_convert_300_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(300), "CCC")

    def test_convert_321_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(321), "CCCXXI")

    def test_convert_432_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(432), "CDXXXII")

    def test_convert_543_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(543), "DXLIII")

    def test_convert_654_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(654), "DCLIV")

    def test_convert_765_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(765), "DCCLXV")

    def test_convert_876_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(876), "DCCCLXXVI")

    def test_convert_987_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(987), "CMLXXXVII")

    def test_convert_999_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(999), "CMXCIX")

    def test_convert_1000_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(1000), "M")

    def test_convert_1234_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(1234), "MCCXXXIV")

    def test_convert_1666_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(1666), "MDCLXVI")

    def test_convert_2000_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(2000), "MM")

    def test_convert_2345_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(2345), "MMCCCXLV")

    def test_convert_3000_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(3000), "MMM")

    def test_convert_3456_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(3456), "MMMCDLVI")

    def test_convert_3999_to_roman_string(self):
        self.assertEqual(RomanNumerals.int_to_roman_string(3999), "MMMCMXCIX")

    def test_parse_empty_string_raises_error(self):
        self.assertRaises(ValueError, RomanNumerals.roman_string_to_int, "")

    def test_parse_IIII_raises_error(self):
        self.assertRaises(ValueError, RomanNumerals.roman_string_to_int, "IIII")

    def test_parse_MMMM_raises_error(self):
        self.assertRaises(ValueError, RomanNumerals.roman_string_to_int, "MMMM")

    def test_parse_IVXLCDM_raises_error(self):
        self.assertRaises(ValueError, RomanNumerals.roman_string_to_int, "IVXLCDM")

    def test_convert_I_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("I"), 1)

    def test_convert_II_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("II"), 2)

    def test_convert_IV_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("IV"), 4)

    def test_convert_V_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("V"), 5)

    def test_convert_VI_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("VI"), 6)

    def test_convert_VII_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("VII"), 7)

    def test_convert_VIII_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("VIII"), 8)

    def test_convert_IX_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("IX"), 9)

    def test_convert_X_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("X"), 10)

    def test_convert_XX_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("XX"), 20)

    def test_convert_XXI_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("XXI"), 21)

    def test_convert_XXXII_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("XXXII"), 32)

    def test_convert_XLIII_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("XLIII"), 43)

    def test_convert_LIV_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("LIV"), 54)

    def test_convert_LXV_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("LXV"), 65)

    def test_convert_LXXVI_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("LXXVI"), 76)

    def test_convert_LXXXVII_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("LXXXVII"), 87)

    def test_convert_XCVIII_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("XCVIII"), 98)

    def test_convert_XCIX_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("XCIX"), 99)

    def test_convert_C_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("C"), 100)

    def test_convert_CC_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("CC"), 200)

    def test_convert_CCC_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("CCC"), 300)

    def test_convert_CCCXXI_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("CCCXXI"), 321)

    def test_convert_CDXXXII_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("CDXXXII"), 432)

    def test_convert_DXLIII_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("DXLIII"), 543)

    def test_convert_DCLIV_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("DCLIV"), 654)

    def test_convert_DCCLXV_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("DCCLXV"), 765)

    def test_convert_DCCCLXXVI_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("DCCCLXXVI"), 876)

    def test_convert_CMLXXXVII_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("CMLXXXVII"), 987)

    def test_convert_CMXCIX_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("CMXCIX"), 999)

    def test_convert_M_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("M"), 1000)

    def test_convert_MCCXXXIV_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("MCCXXXIV"), 1234)

    def test_convert_MDCLXVI_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("MDCLXVI"), 1666)

    def test_convert_MM_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("MM"), 2000)

    def test_convert_MMCCCXLV_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("MMCCCXLV"), 2345)

    def test_convert_MMM_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("MMM"), 3000)

    def test_convert_MMMCDLVI_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("MMMCDLVI"), 3456)

    def test_convert_MMMCMXCIX_to_int(self):
        self.assertEqual(RomanNumerals.roman_string_to_int("MMMCMXCIX"), 3999)

if __name__ == '__main__':
    unittest.main()
