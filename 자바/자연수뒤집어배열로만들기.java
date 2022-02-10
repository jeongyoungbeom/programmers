public class 자연수뒤집어배열로만들기 {
    public int[] solution(long n) {
        String str = ""+n;
        int num = str.length();
        int[] answer = new int[num];

        for (int i = 0; i < num; i++) {
            answer[i] = (int)(n%10);
            n/=10;
        }
        return answer;
    }
}
