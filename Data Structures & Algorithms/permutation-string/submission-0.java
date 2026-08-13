class Solution {
    public boolean checkInclusion(String s1, String s2) {
        //permutation == same hashmap
        // e.g {c: 1, a: 1, b:1} == {a:1, b:1, c:1}

        //sliding window

        boolean permutationExists = false;
        int left = 0;

        Map<Character, Integer> s1map = new HashMap<>();
        Map<Character, Integer> s2map = new HashMap<>();
        //establish s1map
        for (int i = 0; i < s1.length(); i++)
        {
            s1map.put(s1.charAt(i), s1map.getOrDefault(s1.charAt(i),0) + 1);
        }


        if (s1.length() > s2.length()) return false;
        
        // first window
        int k = s1.length();

        for (int i = 0; i < k; i ++)
        {
            s2map.put(s2.charAt(i), s2map.getOrDefault(s2.charAt(i),0) + 1);      
        }

        if (s1map.equals(s2map))
        {
            permutationExists = true;
        }


        for (int i = k; i < s2.length(); i++)
        {
            s2map.put(s2.charAt(i), s2map.getOrDefault(s2.charAt(i),0) + 1);
            s2map.put(s2.charAt(i - k), s2map.getOrDefault(s2.charAt(i - k),0) - 1);
            if (s2map.get(s2.charAt(i-k)) <= 0)
            {
                s2map.remove(s2.charAt(i - k));
            }

            if (s1map.equals(s2map))
            {
                permutationExists = true;
            }
             // remove last char
        }


        
        
        return permutationExists;

        

    }
}
