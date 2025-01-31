from manim import *
import numpy as np

class NewtonMethod(Scene):
    def construct(self):
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