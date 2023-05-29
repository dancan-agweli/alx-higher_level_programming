#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - provides data on pobject
 * @p: the PyObject
 */

void print_python_float(PyObject *p)
{
	double x = 0;
	char *y = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	x = ((PyFloatObject *)p)->ob_fval;
	y = PyOS_double_to_string(x, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", y);
}

/**
 * print_python_bytes - provide data on pyobject
 * @p: the PyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t ln = 0, x = 0;
	char *st = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	ln = PyBytes_Size(p);
	printf("  size: %zd\n", ln);
	st = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", st);
	printf("  first %zd bytes:", ln < 10 ? ln + 1 : 10);
	if (x < ln + 1 && x < 10)
	{
		printf(" %02hhx", st[x]);
		x++;
	}
	printf("\n");
}

/**
 * print_python_list - provide fata
 * @p: the PyObject
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t ln = 0;
	PyObject *item;
	int x = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		ln = PyList_GET_SIZE(p);

		printf("[*] Size of the Python List = %zd\n", ln);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (x < ln)
		{
			item = PyList_GET_ITEM(p, x);
			printf("Element %d: %s\n", x, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			x++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
