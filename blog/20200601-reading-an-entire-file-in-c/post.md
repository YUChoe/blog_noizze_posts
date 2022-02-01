
```C
char* getBlkStatData() {
    char *fcontent = NULL;

    FILE* fp = fopen("/tmp/instance.stat", "r");

    fseek(fp, 0, SEEK_END);
    long size = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    fcontent = (char *)malloc(size);
    fread(fcontent, 1, size, fp);
    fclose(fp);

    return fcontent;
}
```

