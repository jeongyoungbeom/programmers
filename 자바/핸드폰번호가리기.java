public class 핸드폰번호가리기 {
    public String solution(String phone_number) {
        String answer = "";
        int lenNum = (phone_number.length())-4;
        for (int i = 0; i < phone_number.length(); i++) {
            if (i < lenNum){
                answer += "*";
            }else{
                answer += phone_number.charAt(i);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        핸드폰번호가리기 qq = new 핸드폰번호가리기();

        System.out.println(qq.solution("01055275957"));
    }
}
