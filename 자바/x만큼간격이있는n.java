public class x만큼간격이있는n {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = x*(i+1);
        }
        return answer;
    }
}
