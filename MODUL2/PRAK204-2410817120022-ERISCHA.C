#include <stdio.h>
float hitungVolume(float r, float h){
    return 22.0/7.0 * r * r * h;
}
float hitungLuas(float r, float h){
    return 2 * 22.0/7.0 * r * (r + h);
}
float hitungKeliling(float r, float h){
    return 2 * 22.0/7.0 * r;
}
int main(){
    float r, h;
    printf("jari-jari: ");
    scanf("%f", &r);
    printf("tinggi: ");
    scanf("%f", &h);
    float volume = hitungVolume(r, h);
    float luas = hitungLuas(r, h);
    float keliling = 
    hitungKeliling(r, h);
    printf("Volume = %.2f\n", volume);
    printf("Luas = %.2f\n", luas);
    printf("keliling = %.2f", keliling);
return 0;
}