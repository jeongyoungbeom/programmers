public class 콜라츠추측 {
    public int solution(int num) {
        long number = num;
        for (int i = 0; i < 500; i++) {
            if (number == 1){
                return i;
            }
            number = (number % 2 == 0) ? number/2 : number*3+1;
        }
        return -1;
    }

    public static void main(String[] args) {
        콜라츠추측 qq = new 콜라츠추측();
        System.out.println(qq.solution(626331));
    }
}
