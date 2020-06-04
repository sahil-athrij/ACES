#define FB_MAX 100

#define FIZZ 0x01
#define BUZZ 0x02

__global__ void fizzbuzz(unsigned char *fbValues) {
        int tid = blockIdx.x;
        if (tid < FB_MAX) {
                fbValues[tid] = 0;
                fbValues[tid] = fbValues[tid] | (tid % 3 == 0 ? FIZZ : 0);
                fbValues[tid] = fbValues[tid] | (tid % 5 == 0 ? BUZZ : 0);
        }
}
int main() {
        cudaEvent_t start, stop;
        float elapsedTime;

        cudaEventCreate(&start);
        cudaEventCreate(&stop);

        unsigned char fbValues[FB_MAX];
        unsigned char* devFbValues;

        cudaEventRecord(start, 0);
        cudaMalloc((void**) &devFbValues, FB_MAX * sizeof(unsigned char));
        fizzbuzz<<<FB_MAX,1>>>(devFbValues);
        cudaMemcpy(&fbValues, devFbValues, FB_MAX * sizeof(unsigned char), cudaMemcpyDeviceToHost);
        cudaEventRecord(stop, 0);
        cudaEventSynchronize(stop);
        cudaEventElapsedTime(&elapsedTime, start, stop);

        // clean up
        cudaFree(devFbValues);
        cudaEventDestroy(start);
        cudaEventDestroy(stop);

        // Print out the results
        int i;
        for (i = 0; i < FB_MAX; i++) {
                std::stringstream s;
                s << i << " ";
                
                if (fbValues[i] & FIZZ) {
                        s << "Fizz ";
                }
                if (fbValues[i] & BUZZ) {
                        s << "Buzz";
                }

                std::cout << s.str() << std::endl;
        }

        std::cout << "Device Time: " << std::setprecision(5) << elapsedTime << " ms" << std::endl;

        return 0;
}
