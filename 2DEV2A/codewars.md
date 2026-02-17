## Exercices de codewars en Java

### Exercice 1:

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples 16:

```
--> 1 + 6 = 7 942
--> 9 + 4 + 2 = 15
--> 1 + 5 = 6 132189
--> 1 + 3 + 2 + 1 + 8 + 9 = 24
--> 2 + 4 = 6 493193
--> 4 + 9 + 3 + 1 + 9 + 3 = 29
--> 2 + 9 = 11
--> 1 + 1 = 2 en java

```

<b>Algo:</b>

```
int digitalRoot(int n)
    while >= n
        int somme = 0
        while n > 0
            somme = n + (n % 10)
            n/10
        n = somme
    retturn n


```

<b>Java:</b>

```
public class Droot{

    public static int digital_root(int n) {
        while (n>=10){
            int somme = 0;
            while(n>0){
                somme = n + (n%10);
                n /= 10
            }
            n = somme;
        return n;
        }
    }

}

```

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples

```
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

```

<b>Algo:</b>

```
String reverseWords(String original)

String resultat = ""
String mot = ""

for i from 0 to original.length() - 1
    char c = original.charAt(i)

    if c == ' '
        resultat = resultat + inverser(mot)
        resultat = resultat + " "
        mot = ""
    else
        mot = mot + c

resultat = resultat + inverser(mot)

return resultat
```

<b>Java:</b>

```
public class Kata {
  public static String reverseWords(final String original) {
    String[] words = original.split(" ", -1);
    String[] res = new String[words.length];
    for(int i = 0; i < words.length; i++){
      StringBuilder reversed = new StringBuilder();
      for (int j = words[i].length() - 1; j >= 0; j--){
        reversed.append(words[i].charAt(j));

      }
      res[i]= reversed.toString();
    }
    return String.join(" ", res);
 }
}
```
