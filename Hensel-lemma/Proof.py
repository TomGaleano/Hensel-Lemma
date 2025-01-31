from manim import *

class HenselsLemma(Scene):
    def construct(self):
        # --- Título ---
        title = MathTex(r"\text{Lema de Hensel}", font_size=60).to_edge(UP)
        self.play(Write(title))
        self.wait(5)

        # --- Enunciado ---
        statement = VGroup(
            MathTex(r"\text{Si }f(x)\in\mathbb Z[x]\text{ y }a\in\mathbb Z\text{ es tal que }f(a)\equiv0\mod p^n", font_size=36),
            MathTex(r"\text{(con }p\text{ primo y }n\geq 1\text{) y }f'(a)\not\equiv0\mod p\text{. Entonces existe un}", font_size=36),
            MathTex(r"\text{único }t\in\{0,1,\dots,p-1\}\text{ tal que }f(a+tp^n)\equiv0\mod p^{n+1}", font_size=36),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 0.5)
        
        self.play(Write(statement))
        self.wait(16)
        self.play(FadeOut(statement))

        # --- Condiciones ---
        conditions_title = MathTex(r"\text{Condiciones del Lema:}", font_size=48).to_edge(UP)
        self.play(ReplacementTransform(title, conditions_title))

        conditions = VGroup(
            MathTex(r"f(a) \equiv 0 \pmod{p^n}", font_size=42),
            MathTex(r"f'(a) \not\equiv 0 \pmod{p}", font_size=42)
        ).arrange(RIGHT, buff=0.5).move_to(UP * 1)
        
        self.play(Write(conditions))
        self.wait(12)

        # --- Demostración ---
        proof_title = MathTex(r"\text{Demostración:}", font_size=48).to_edge(UP)
        self.play(ReplacementTransform(conditions_title, proof_title))

        # Mover condiciones al borde inferior
        self.play(conditions.animate.shift(DOWN * 4.5))

        # --- Paso 1: Escribir f(x) en su serie de Taylor ---

        taylor_series = MathTex(r"f(x) = \sum_{i=0}^{\infty}\dfrac{f^{(i)}(a)}{i!}(x-a)^i", font_size=36)
        taylor_series.move_to(UP * 2)
        self.play(Write(taylor_series))

        self.wait(12)

        # --- Paso 2: Evaluar f(a+tp^n) ---

        taylor_series_evaluated = MathTex(r"f(a+tp^n) = \sum_{i=0}^{\infty}\dfrac{f^{(i)}(a)}{i!}(tp^n)^i", font_size=36) 
        taylor_series_evaluated.move_to(UP * 2)
        self.play(Transform(taylor_series, taylor_series_evaluated))

        self.wait(12)

        # --- Paso 3: Factorizar p^n+1 ---

        taylor_series_evaluated_factored = MathTex(r"f(a+tp^n) = f(a)+f'(a)tp^n+\sum_{i=2}^{\infty}\dfrac{f^{(i)}(a)}{i!}t^ip^{ni}", font_size=36)
        taylor_series_evaluated_factored.move_to(UP * 2)
        self.play(Transform(taylor_series, taylor_series_evaluated_factored))

        self.wait(12)

        # --- Paso 4: Evaluar f(a+tp^n) en módulo p^{n+1} ---
        taylor_series_evaluated_mod_p = MathTex(r"f(a+tp^n) \equiv f(a) + f'(a)tp^n \pmod{p^{n+1}}", font_size=36)
        taylor_series_evaluated_mod_p.move_to(UP * 2)
        self.play(Transform(taylor_series, taylor_series_evaluated_mod_p))

        self.wait(12)

        # --- Paso 5: Mostrar equivalencias de que t sea una solución al problema ---
        equivalence_1 = MathTex(r"t \text{ es una solución al problema }\iff", font_size=36)
        equivalence_2 = MathTex(r"f(a)+f'(a)tp^n\equiv 0 \pmod{p^{n+1}}", font_size=36)

        equivalence_1.move_to(LEFT * 3)
        equivalence_2.next_to(equivalence_1, RIGHT)

        self.play(Write(equivalence_1))
        self.play(Write(equivalence_2))

        self.wait(12)

        equivalence_3 = MathTex(r"f(a)+f'(a)tp^n=k_1p^{n+1},\ k_1\in\mathbb Z", font_size=36)
        equivalence_3.next_to(equivalence_1, RIGHT)

        self.play(Transform(equivalence_2, equivalence_3))

        self.wait(12)

        equivalence_4 = MathTex(r"k_2p^n+f'(a)tp^n=k_1p^{n+1},\ k_i\in\mathbb Z", font_size=36)
        equivalence_4.next_to(equivalence_1, RIGHT)

        self.play(Transform(equivalence_2, equivalence_4))

        self.wait(12)

        equivalence_5 = MathTex(r"k_2+f'(a)t=k_1p", font_size=36)
        equivalence_5.next_to(equivalence_1, RIGHT)

        self.play(Transform(equivalence_2, equivalence_5))

        self.wait(12)

        equivalence_6 = MathTex(r"f'(a)t\equiv -k_2 \pmod{p}", font_size=36)
        equivalence_6.next_to(equivalence_1, RIGHT)

        self.play(Transform(equivalence_2, equivalence_6))

        self.wait(12)

        # --- Paso 6: Terminar la prueba ---

        end_proof = MathTex(r"\text{Por lo tanto, existe una solución única }t\in\{0,1,\dots,p-1\}\text{ al problema.}", font_size=36)
        end_proof.move_to(DOWN)

        self.play(Write(end_proof))

        end_proof_square = MathTex(r"\blacksquare", font_size=36)
        end_proof_square.to_corner(DR)
        self.play(Write(end_proof_square))



        self.wait(4)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        