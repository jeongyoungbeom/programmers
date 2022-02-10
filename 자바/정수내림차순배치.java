import java.util.Arrays;
import java.util.Collections;

public class 정수내림차순배치 {
    public long solution(long n) {
        String str = Long.toString(n);

        String[] arrStr = str.split("");
        Arrays.sort(arrStr, Collections.reverseOrder());

        str = String.join("", arrStr);

        long answer = Long.parseLong(str);
        return answer;
    }
}
