from manim import *
from Introduction import HenselIntroduction
from NewtonMethod import NewtonMethod
from AnotherLagrangeTheorem import LagrangeTheorem
from Proof import HenselsLemma
from Examples import Examples

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 60

class MainVideo(Scene):
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

        # Texto inicial
        question = MathTex(r"\text{¿Cómo aproximamos }\sqrt{7}\text{ en }\mathbb{R}\text{?}", font_size=48).to_edge(UP)
        self.play(Write(question))
        self.wait(12)
        self.play(FadeOut(question))

        # Fórmula del método de Newton
        newton_formula = MathTex("x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}").to_edge(UP)
        self.play(Write(newton_formula))
        self.wait(12)

        # Define axes
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-2, 10, 2],
            axis_config={"color": WHITE},
        )
        axes_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=36),
            y_label=MathTex("y", font_size=36)
        )
        self.play(Create(axes), Write(axes_labels))

        # Define function and its derivative
        def f(x):
            return x**2 - 7
        
        def f_prime(x):
            return 2*x
        
        # Create graph
        graph = axes.plot(lambda x: f(x), color=BLUE)
        self.play(Create(graph))

        # Number of iterations
        num_iterations = 9  # Aumentamos el número de iteraciones

        # Initial point
        x = 3.0
        x_point = axes.coords_to_point(x, 0)
        initial_dot = Dot(x_point, color=RED)
        

        # Iteraciones del método de Newton
        c_i = 0  # Inicializa c_i
        c_i_text = MathTex(f"c_{c_i} = {x:.12f}", font_size=48).move_to(ORIGIN)  # 8 cifras decimales
        self.play(Write(c_i_text))

        curves = []  # Lista para almacenar las curvas antiguas

        for i in range(num_iterations):
            x_next = x - f(x) / f_prime(x)

            vertical_line = Line(
                axes.coords_to_point(x, 0),
                axes.coords_to_point(x, f(x)),
                color=YELLOW
            )
            self.play(Create(vertical_line))

            slope = f_prime(x)
            tangent_line = Line(
                axes.coords_to_point(x - 0.5, f(x) - 0.5 * slope),
                axes.coords_to_point(x + 0.5, f(x) + 0.5 * slope),
                color=GREEN
            )
            self.play(Create(tangent_line))

            x_next_point = axes.coords_to_point(x_next, 0)
            x_next_dot = Dot(x_next_point, color=RED)
            self.play(Create(x_next_dot))

            x = x_next

            # Actualiza c_i y su texto
            c_i += 1
            new_c_i_text = MathTex(f"c_{c_i} = {x:.12f}...", font_size=48).move_to(ORIGIN)  # 8 cifras decimales
            self.play(TransformMatchingTex(c_i_text, new_c_i_text))
            c_i_text = new_c_i_text

            # Dibuja la nueva curva y desvanece la tercera más antigua
            new_graph = axes.plot(lambda x_val: f(x_val), color=BLUE)
            curves.append(new_graph)
            self.play(Create(new_graph))

            if len(curves) > 3:
                self.play(FadeOut(curves[-4]))  # Desvanece la tercera curva más antigua

            # Espera entre actualizaciones de c_i (tiempo variable)
            if i == 1:
                wait_time = 3  # Espera 3 segundos para la segunda actualización
            elif i > 6:
                wait_time = 0.5  # Espera 0.5 segundos desde la séptima actualización
            else:
                wait_time = 0.7  # Espera 1 segundo para las demás actualizaciones
            self.wait(wait_time)

        # Reemplazo de c_10 por c_∞ = √7 al final
        c_inf_text = MathTex("c_{\\infty} = \\sqrt{7}").move_to(ORIGIN)
        self.play(TransformMatchingTex(c_i_text, c_inf_text))  # Transición suave

        self.wait(12)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

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


        # Write first corollary

        corollary1 = MathTex(r"x^{p-1}\equiv1\pmod{p^n}\text{ tiene exactamente }p-1\text{ raíces para todo primo }p\text{ y }n\geq1.", font_size=36)

        self.play(Write(corollary1))

        self.wait(12)

        self.play(FadeOut(corollary1))

        # Write second corollary

        corollary2 = MathTex(r"\text{Gal}(x^n-x-1/\mathbb Q)\cong S_n,\text{ para todo }n\geq 1.", font_size=36)

        self.play(Write(corollary2))

        self.wait(12)

        

        self.play(FadeOut(corollary2))

        # Crear plano complejo
        plane = ComplexPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        ).add_coordinates()

        # Título inicial
        title = MathTex(r"x^n - x - 1 = 0", font_size=48).to_edge(UP)
        
        self.play(
            Create(plane),
            Write(title)
        )
        self.wait(1)

        # Lista para almacenar dots anteriores
        prev_dots = None

        # Para cada grado n
        for n in range(2, 11):
            # Actualizar título
            new_title = MathTex(f"x^{{{n}}} - x - 1 = 0", font_size=48).to_edge(UP)
            
             # Calcular raíces usando numpy en lugar de scipy
            coeffs = np.zeros(n + 1)
            coeffs[n] = 1  # x^n
            coeffs[1] = -1  # -x
            coeffs[0] = -1  # -1
            polynomial_roots = np.roots(coeffs)


            # Crear dots para las raíces
            dots = VGroup(*[
                Dot(
                    plane.n2p(complex(root.real, root.imag)),
                    color=YELLOW
                )
                for root in polynomial_roots
            ])

            # Añadir números
            labels = VGroup(*[
                MathTex(f"{complex(root.real, root.imag):.2f}", font_size=24)
                .next_to(dot, UR, buff=0.1)
                for root, dot in zip(polynomial_roots, dots)
            ])

            # Animación
            if prev_dots is None:
                self.play(
                    Transform(title, new_title),
                    Create(dots),
                    Write(labels)
                )
            else:
                self.play(
                    Transform(title, new_title),
                    Create(dots),
                    Write(labels)
                )

            self.wait(2)
            
            # Borrar raíces y etiquetas antes de la siguiente iteración
            self.play(
                FadeOut(dots),
                FadeOut(labels)
            )
            
            self.wait(0.5)

        # Final
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )