const API_URL = process.env.NEXT_PUBLIC_API_URL;

console.log('API_URL:', API_URL);

export async function fetchTodos() {
  try {
    const response = await fetch(`${API_URL}/todos`);
    if (!response.ok) {
      throw new Error('Error al obtener los todos');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching todos:', error);
  }
}
