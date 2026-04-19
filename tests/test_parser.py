import unittest
from chapter_directory_parser import parse_chapter_blueprint

class TestChapterParser(unittest.TestCase):
    def test_parse_chinese_format(self):
        text = """
第1章 - 启程
本章定位：开篇
核心作用：引入主角
悬念密度：一般
伏笔操作：埋下玉佩线索
认知颠覆：★☆☆☆☆
本章简述：主角离开家乡。
"""
        results = parse_chapter_blueprint(text)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["chapter_number"], 1)
        self.assertEqual(results[0]["chapter_title"], "启程")
        self.assertEqual(results[0]["chapter_role"], "开篇")

    def test_parse_english_format(self):
        text = """
Chapter 2 - The Discovery
Chapter Position: Middle
Core Purpose: Plot thickening
Suspense Density: High
Foreshadowing: The mysterious letter
Plot Twist Level: ★★★☆☆
Chapter Summary: They found the secret passage.
"""
        results = parse_chapter_blueprint(text)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["chapter_number"], 2)
        self.assertEqual(results[0]["chapter_title"], "The Discovery")
        self.assertEqual(results[0]["chapter_role"], "Middle")

if __name__ == "__main__":
    unittest.main()
