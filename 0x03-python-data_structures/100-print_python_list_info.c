#include <Python.h>

/**
 * print_python_list_info - adds new node at the end of a listint_t
 * @p: pointer PyObject
 */

void print_python_list_info(PyObject *p)
{
	long int list_size;
	int i;
	PyListObject *list_obj;

	list_size = PyList_Size(p);
	list_obj = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", list_obj->allocated);
	for (i = 0; i < list_size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(list_obj->ob_item[i])->tp_name);
}
