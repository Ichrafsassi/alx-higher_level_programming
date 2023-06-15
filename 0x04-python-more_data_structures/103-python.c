#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
	char *ch;
	long int size, i, lmt;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	ch = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", ch);

	if (size >= 10)
		lmt = 10;
	else
		lmt = size + 1;

	printf("  first %ld bytes:", lmt);

	for (i = 0; i < lmt; i++)
		if (ch[i] >= 0)
			printf(" %02x", ch[i]);
		else
			printf(" %02x", 256 + ch[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: no return
 */

void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
