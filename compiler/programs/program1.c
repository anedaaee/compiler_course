int main() {
    //char c = 'x';
    int a = 2;
    int b = a + 3;
    //int b = a + c;
   // int c = a * b;

    a = 2;
    a = b;
    //a = 'c';
    //f = d;
    b = c | a;
    a = c - b;


    if(c < 12) {
        a = 1;
    } else  {
        a = 2;
    }


    while (a > 0)
    {
        if(a == 12) {
            break;
        } else {
            continue;
        }
        a = a - 1;
    }

}