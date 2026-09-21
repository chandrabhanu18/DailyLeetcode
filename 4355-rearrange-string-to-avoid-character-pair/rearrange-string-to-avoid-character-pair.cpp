class Solution {
public:
    string rearrangeString(string s, char x, char y) {
        string yy="";
        string other="";
        string xx="";

        for(char c:s)
            {
                if(c==x)
                {
                    xx+=c;
                }
                else if(c==y)
                {
                    yy+=c;
                }
                else
                {
                    other+=c;
                }
            }
        string ans=yy+xx+other;
        return ans;
    }
};