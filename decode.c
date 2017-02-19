#include<stdio.h>
unsigned int d[256] =  { 16, 20, 26, 28, 32, 38, 40, 44, 48, 55, 56, 60, 67, 68, 75, 77, 83, 84, 91, 93, 97, 102, 106, 109, 112, 117, 122, 125, 131,
132, 139, 141, 147, 148, 155, 157, 161, 166, 170, 173, 176, 181, 186, 189, 192, 196, 203, 205, 209, 212, 218, 221, 227, 228,
235, 237, 243, 244, 251, 253, 259, 261, 267, 269, 272, 277, 282, 285, 288, 292, 299, 301, 305, 308, 314, 317, 323, 324, 331,
333, 339, 340, 347, 349, 355, 357, 363, 365, 368, 373, 378, 381, 387, 388, 395, 397, 402, 407, 410, 413, 419, 420, 427, 429,
434, 439, 442, 445, 451, 452, 459, 461, 466, 471, 474, 477, 483, 484, 491, 493, 498, 503, 506, 509, 514, 516, 520, 525,0,};
unsigned char flag_tbl[256] = {0,};
unsigned char frame_tbl[64] = {0,};
void construct_data_broadcast(unsigned int data)
{ 
    // 1111 11 00 a 10 b 11 c 12  11111111
   unsigned int byte_index =  (data & 0xfff0) >> 4;
   unsigned int index = data >>2;
   unsigned int bit_index = (data & 0x0c) >> 2;
   unsigned int bit_data = data & 0x03;

   if(flag_tbl[index] == 0 )
   {
        flag_tbl[index] = 1;
        //frame_tbl[byte_index] |= (0x03 << (bit_index * 2));
        //printf("%d\n",bit_index);

        frame_tbl[byte_index] |= (bit_data << (bit_index * 2));
   }
}
void construct_data_multicast(unsigned char *data,unsigned char *result)
{
    unsigned int index = data[0];

}
int main()
{
    printf("hello world\n");

  
    for(int i = 0; i< 256;i++)
    {
        if(d[i] > 0)
        {
            construct_data_broadcast(d[i]);
        }
    }

    for(int i = 0; i< 256;i++)
    {
        if(i % 32 == 0)
        {
            printf("\n");
        }
        printf("%d ",d[i]);
    }

    printf("\n");
    for(int i = 0; i< 256;i++)
    {
        if(i%32 == 0)
        {
            printf("\n");
        }
        printf("%d ",flag_tbl[i]);
    }

    printf("\n");
    for(int i = 0; i< 256;i++)
    {
        if(i%32 == 0)
        {
            printf("\n");
        }
        printf("%c ",frame_tbl[i]);
    }
    return 0;
}