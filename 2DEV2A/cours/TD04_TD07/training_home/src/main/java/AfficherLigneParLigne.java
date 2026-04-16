

public class AfficherLigneParLigne{

    public static void afficherLigneParLigne(int[][] tab) {
        if (tab == null) {
            System.out.println("Le tableau est null.");
            return;
        }

        for (int lg = 0; lg < tab.length; lg++) {
            if (tab[lg] == null) {
                System.out.println("Ligne " + lg + " est null.");
                continue;
            }

            for (int col = 0; col < tab[lg].length; col++) {
                System.out.print(tab[lg][col] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] tableau = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        afficherLigneParLigne(tableau);
    }
}