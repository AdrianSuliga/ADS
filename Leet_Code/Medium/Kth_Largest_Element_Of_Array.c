int partition(int* nums, int size, int left, int right, int p_index);
void swap(int* nums, int i, int j);
int findKthLargest(int* nums, int numsSize, int k) {
    int left = 0, right = numsSize - 1;
    k--;
    while (1)
    {
        int pivot = (left + right) / 2;
        pivot = partition(nums, numsSize, left, right, pivot);
        if (pivot == k)
            return nums[k];
        else if (k < pivot)
            right = pivot - 1;
        else
            left = pivot + 1;
    }
}

int partition(int* nums, int size, int left, int right, int p_index)
{
    int pivot = right;
    swap(nums, p_index, right);
    int ind = left - 1;
    for (int i = left; i < right; i++)
    {
        if (nums[i] > nums[pivot])
        {
            ind++;
            swap(nums, i, ind);
        }
    }
    ind++;
    swap(nums, ind, pivot);
    return ind;
}

void swap(int* nums, int i, int j)
{
    int buffor = nums[i];
    nums[i] = nums[j];
    nums[j] = buffor;
}

int main()
{
    return 0;
}