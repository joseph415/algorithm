package practice;

public class StringConverter {
    public static void main(String[] args) {
        String a = "testTEST";
        StringBuilder stringBuilder = new StringBuilder();

        for (int i = 0; i < a.length(); i++) {
            final char c = a.charAt(i);
            if (65 <= c && c <= 90) {
                stringBuilder.append(String.valueOf(c).toLowerCase());
            } else if (97 <= c && c <= 122) {
                stringBuilder.append(String.valueOf(c).toUpperCase());
            }
            else {
                stringBuilder.append(c);
            }
        }
        System.out.println(stringBuilder);
    }
}
