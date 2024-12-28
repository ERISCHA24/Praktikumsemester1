#include <stdio.h> 
int main() { 
    int waktu; 
    int hari, jam, menit, detik; 
    printf("Masukkan jumlah detik: "); 
    scanf("%d", &waktu); 
    hari = (waktu / 86400); 
    jam = (waktu % 86400) / 3600;              
    menit = (waktu % 3600) / 60;    
    detik = waktu % 60;              
    printf("%d hari %d:%d:%d\n", hari, jam, menit, detik); 
    return 0; 
}