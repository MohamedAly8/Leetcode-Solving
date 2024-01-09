class Solution {
    public String intToRoman(int num) {
        

        String[] romans = new String[]{"M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV", "I"};
        Integer[] ints = new Integer[]{1000, 900, 500,400,100,90,50,40,10,9,5,4,1};

        int idx = 0;
        List<String> roman = new ArrayList();
        while(num > 0){
            if (num >= ints[idx]){
                num = num - ints[idx];
                roman.add(romans[idx]);
            }
            else {
                idx += 1;
            }

        }

        String s = String.join("", roman);
        return s;

    }
}