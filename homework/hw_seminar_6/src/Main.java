//Написать программу на любом языке в любой парадигме для
//бинарного поиска. На вход подаётся целочисленный массив и
//число. На выходе - индекс элемента или -1, в случае если искомого
//элемента нет в массиве.


public class Main {
    public static void main(String[] args) {
        int[] array =  {1,3,4,6,7,8,10,13,14};
        int key = 4;
        int index = binarySearch(array, key, 0, array.length - 1);
        System.out.println(index);
    }

    public static int binarySearch(int[] array, int key, int low, int high) {
        int index = -1;

        while (low <= high) {
            int middle = (low + high) / 2;
            if (array[middle] < key) {
                low = middle + 1;
            } else if (array[middle] > key) {
                high = middle - 1;
            } else if (array[middle] == key) {
                index = middle;
                break;
            }
        }
        return index;
    }
}