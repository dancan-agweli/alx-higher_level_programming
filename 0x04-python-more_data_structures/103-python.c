#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - python lists
 *
 * @p: ...
 */
void print_python_bytes(PyObject *p)
{
	unsigned int x, l, uz;
	char *ss;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	uz = ((PyVarObject *)p)->ob_size;
	ss = ((PyBytesObject *)p)->ob_sval;
	l =  uz + 1 > 10 ? 10 : uz + 1;
	printf("  size: %lu\n", uz);
	printf("  trying string: %s\n", ss);
	printf("  first %lu bytes: ", l);
	for (x = 0; x < l; x++)
		printf("%02hhx%s", ss[x], x + 1 < l ? " " : "");
	printf("\n");
}

/**
 * print_python_list - write python lists
 *
 * @p: ...
 */
void print_python_list(PyObject *p)
{
	int y;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (y = 0; y < ((PyVarObject *)p)->ob_size; y++)
	{
		printf("Element %d: %s\n", y,
			((PyListObject *)p)->ob_item[y]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[y]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[y]);

	}
}
