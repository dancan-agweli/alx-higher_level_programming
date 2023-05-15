#include <Python.h>

/**
 * print_python_list_info - Data of the python in the lsits
 * @p: ...
 */
void print_python_list_info(PyObject *p)
{
	int x, malo, y;
	PyObject *dan;

	x = Py_SIZE(p);
	malo = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", x);
	printf("[*] Allocated = %d\n", malo);
	for (y = 0; y < x; y++)
	{
		printf("Element %d: ", y);

		dan = PyList_GetItem(p, y);
		printf("%s\n", Py_TYPE(dan)->tp_name);
	}
}

