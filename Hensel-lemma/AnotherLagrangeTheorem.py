from manim import *

class LagrangeTheorem(Scene):
    def construct(self):
        # --- Título Principal ---
        title = MathTex(r"\text{Teorema de Lagrange}", font_size=60).to_edge(UP)
        self.play(Write(title))
        self.wait(6)

        # --- Enunciado del Teorema ---
        theorem = VGroup(
            MathTex(r"\text{Si }f(x)\text{ es un polinomio con coeficientes enteros,}", font_size=36),
            MathTex(r"\text{y el coeficiente principal no es divisible por un primo }p\text{,}", font_size=36),
            MathTex(r"\text{entonces la congruencia }f(x) \equiv 0 \pmod{p}", font_size=36),
            MathTex(r"\text{tiene a lo sumo un número de soluciones igual al grado de }f(x)\text{.}", font_size=36)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 0.5)
        
        self.play(Write(theorem))
        self.wait(12)
        self.play(FadeOut(theorem))

        # --- Caso Base ---
        base_title = MathTex(r"\text{Caso Base (Grado 1)}", font_size=48).to_edge(UP)
        self.play(ReplacementTransform(title, base_title))

        base_eq = MathTex(
            r"f(x) = ax + b", 
            r"\quad(a \not\equiv 0 \pmod{p})", 
            font_size=42
        ).move_to(UP * 1)
        
        self.play(Write(base_eq))

        example = VGroup(
            MathTex(r"2x + 3 \equiv 0 \pmod{5}", font_size=42),
            MathTex(r"\text{Multiplicando por }3 \equiv 2^{-1} \pmod{5}\text{:}", font_size=36)
        ).arrange(DOWN, buff=0.5).next_to(base_eq, DOWN)
        
        self.play(Write(example))

        solution = VGroup(
            MathTex(r"3(2x + 3) &\equiv 0 \pmod{5}"),
            MathTex(r"6x + 9 &\equiv 0 \pmod{5}"),
            MathTex(r"x + 4 &\equiv 0 \pmod{5}"),
            MathTex(r"x &\equiv 1 \pmod{5}")
        ).arrange(DOWN, buff=0.3).next_to(example, DOWN)

        for step in solution:
            self.play(Write(step))
            self.wait(0.5)

        # --- Hipótesis Inductiva ---
        inductive_title = MathTex(r"\text{Hipótesis Inductiva}", font_size=48).to_edge(UP)
        self.play(
            *[FadeOut(mob) for mob in [base_title, base_eq, example, solution]],
            Transform(base_title, inductive_title)
        )

        hypothesis = MathTex(
            r"\text{Suponemos que el teorema es válido para polinomios de grado }k\text{.}\\", font_size=36).move_to(ORIGIN)
        
        self.play(Write(hypothesis))
        self.wait(12)

        # --- Paso Inductivo ---
        inductive_step = MathTex(r"\text{Paso Inductivo (Grado }k+1\text{)}", font_size=48).to_edge(UP)
        self.play(
            FadeOut(hypothesis),
            Transform(inductive_title, inductive_step)
        )

        step_explanation_1 = VGroup(
            MathTex(r"\text{Sea }f(x)\text{ un polinomio de grado }k+1\text{. Consideremos}", font_size=36),
            MathTex(r"a\text{ una raíz de }f(x)\text{ módulo }p\text{i.e. }f(a)\equiv0\mod p\text{.}", font_size=36)
        ).arrange(DOWN, buff=0.3)
        
        step_explanation_1.move_to(UP * 1)
        self.play(Write(step_explanation_1))
        self.wait(12)

        step_explanation_2 = VGroup(
            MathTex(r"\text{Notemos que, }\forall m\in\mathbb Z\text{, }m\text{ es raíz de }f(x)-f(m)\text{ luego}", font_size=36),
            MathTex(r"f(x)-f(m)=(x-m)g(x)\text{ donde }\partial g=k\text{ se puede escribir como:}", font_size=36),
            MathTex(r"f(x) =f(x)-f(a)= (x - a)g(x)", font_size=36),
            MathTex(r"\text{para algún  }g(x)\text{ que por hipótesis tiene a lo más }k\text{ raíces}", font_size=36)
        ).arrange(DOWN, buff=0.3).next_to(step_explanation_1, DOWN)

        self.play(Write(step_explanation_2))
        self.wait(12)

        # --- Conclusión ---
        conclusion_title = MathTex(r"\text{Conclusión}", font_size=48).to_edge(UP)
        self.play(
            FadeOut(step_explanation_1, step_explanation_2, inductive_title),
            Write(conclusion_title)
        )

        conclusion = VGroup(
            MathTex(r"\text{Por inducción, el teorema es válido}", font_size=36),
            MathTex(r"\text{para polinomios de cualquier grado.}", font_size=36)
        ).arrange(DOWN, buff=0.3)
        
        self.play(Write(conclusion))

        end_proof_square = MathTex(r"\blacksquare", font_size=36)
        end_proof_square.to_corner(DR)
        self.play(Write(end_proof_square))

        self.wait(12)

        # --- Nota Final ---
        final_note = VGroup(
            MathTex(r"\text{Observación: La hipótesis de }p\text{ primo es esencial.}", font_size=36),
        ).arrange(DOWN, buff=0.3)

        self.play(
            FadeOut(conclusion),
            Write(final_note)
        )


        self.wait(10)

        # Limpieza final
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1)