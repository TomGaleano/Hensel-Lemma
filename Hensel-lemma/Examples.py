from manim import *
import numpy as np

class Examples(Scene):
    def construct(self):
        
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
