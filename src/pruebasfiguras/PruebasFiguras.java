/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pruebasfiguras;

/**
 *
 * @author Katerin Gomez
 */
public class PruebasFiguras {
public static void main(String[] args) {
        Circulo figura1 = new Circulo(2);
        Rectangulo figura2 = new Rectangulo(1,2);
        Cuadrado figura3 = new Cuadrado(3);
        TrianguloRectangulo figura4 = new TrianguloRectangulo(3,5);
        System.out.println("El area del circulo es = " + figura1. calcularArea());
        System.out.println("El perimetro del circulo es = " + figura1. calcularPerimetro());
        System.out.println();
        System.out.println("El area del rectangulo es = " + figura2. calcularArea());
        System.out.println("El perimetro del rectangulo es = " + figura2. calcularPerimetro());
        System.out.println();
        System.out.println("El area del cuadrado es = " + figura3. calcularArea());
        System.out.println("El perimetro del cuadrado es = " + figura3. calcularPerimetro());
        System.out.println();
        System.out.println("El area del triangulo es = " + figura4. calcularArea());
        System.out.println("El perimetro del triangulo es = " + figura4. calcularPerimetro());
        System.out.println("La hipotenusa del triangulo es = " + figura4. calcularHipotenusa());
        figura4.determinarTipoTriangulo();
    }
    
}