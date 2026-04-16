public class AfficherColonneParColonne {

    public static void afficherColonneParColonne(int[][] tab) {
        if (tab == null || tab.length == 0) {
            System.out.println("Tableau invalide.");
            return;
        }

        for (int col = 0; col < tab[0].length; col++) {
            for (int lg = 0; lg < tab.length; lg++) {
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

        afficherColonneParColonne(tableau);
    }

}
