from manimx import *


class Demo(Scene):
    def construct(self):
        tex = Tex(r"\sum_{i=1}^\infty\frac{1}{i^2}=\frac{\pi^2}{6} \text{你好}")
        text = Text('hello世界')
        textext = TexText(r'$\sum_{i=1}^\infty\frac{1}{i^2}=\frac{\pi^2}{6} 餐廳$')
        textext01 = TexText(r'$\displaystyle\sum_{i=1}^\infty\frac{1}{i^2}=\frac{\pi^2}{6}圖書館$').to_edge(DOWN)
        self.play(Write(VGroup(tex, text, textext, textext01).arrange(DOWN), run_time=6))
        self.wait(5)
