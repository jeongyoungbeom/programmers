import java.util.Arrays;
import java.util.Locale;

public class 이상한문자만들기 {
    public String solution(String s) {
        String answer = "";
        String[] word = s.split("");
        int cnt = 0;

        for (int i = 0; i < word.length; i++) {

            if (word[i].equals(" ")){
                cnt = 0;
            }else{
                if (cnt % 2 == 0){
                    cnt ++;
                    word[i] = word[i].toUpperCase();
                }else{
                    cnt++;
                    word[i] = word[i].toLowerCase();
                }
            }
            answer+= word[i];
        }
        return answer;
    }

    public static void main(String[] args) {
        이상한문자만들기 qq = new 이상한문자만들기();
        System.out.println(qq.solution("try qwe sfa"));
    }
}
