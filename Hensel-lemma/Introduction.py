from manim import *

class HenselIntroduction(Scene):
    def construct(self):
        # Create title text
        title = Text("Lema de Hensel", font_size=40)

        # Place title at the top left corner of the screen
        title.to_corner(UL)


        # Add animation to display title
        self.play(
            Write(title)
        )

        # Add "Motivación:" subtitle below title
        motivation = VGroup(
            MathTex(r"\text{Motivación: Dado un polinomio }f(x)\in\mathbb Q[x]\text{, ¿cómo podemos}", font_size=36),
            MathTex(r"\text{expresar sus raíces en una base }p\text{-ádica para un número primo }p\text{?}", font_size=36)
        ).arrange(DOWN, buff=0.3)

        # Add animation to display motivation
        self.play(
            Write(motivation, run_time=3)
        )

        
        # Wait a few seconds before ending
        self.wait(12)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )