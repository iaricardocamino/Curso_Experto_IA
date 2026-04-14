/**
 * INITIAL DATA
 * Derived from the uploaded CSV for realism.
 */
const inventoryData = [
    { id: 101, category: "Laptop", model: "MacBook Pro M3", serial: "SN-9988-XPL", location: "Almacén A1", stock: 12, status: "Nuevo" },
    { id: 102, category: "Monitor", model: "Dell UltraSharp 27\"", serial: "DS-1122-MON", location: "Oficina 202", stock: 4, status: "Reacondicionado" },
    { id: 103, category: "Periférico", model: "Teclado Logitech MX", serial: "LG-4455-KEY", location: "Almacén B2", stock: 25, status: "Nuevo" },
    { id: 104, category: "Servidor", model: "HP ProLiant Gen10", serial: "HP-0099-SRV", location: "CPD Central", stock: 2, status: "Crítico" },
    { id: 105, category: "Tablet", model: "iPad Air 5th Gen", serial: "IP-7766-TAB", location: "Oficina 105", stock: 8, status: "Nuevo" },
    { id: 106, category: "Redes", model: "Router Cisco ISR", serial: "CS-3322-ROU", location: "Almacén A1", stock: 15, status: "Nuevo" },
    { id: 107, category: "Laptop", model: "Lenovo ThinkPad X1", serial: "LN-8877-LAP", location: "Oficina 202", stock: 3, status: "En reparación" },
    { id: 108, category: "Almacenamiento", model: "SSD Externo 2TB", serial: "SS-5544-DRV", location: "Almacén B2", stock: 40, status: "Nuevo" },
    { id: 109, category: "Monitor", model: "LG Ergo 32\"", serial: "LG-2233-MON", location: "Oficina 301", stock: 6, status: "Nuevo" },
    { id: 110, category: "Periférico", model: "Ratón Ergonómico", serial: "ER-6655-MOU", location: "Almacén A1", stock: 30, status: "Nuevo" }
];

// Constants
const LOW_STOCK_THRESHOLD = 5;

/**
 * Render function: Builds the table rows dynamically
 * @param {Array} data - List of inventory items
 */
const renderTable = (data) => {
    const tbody = document.getElementById('inventoryBody');
    tbody.innerHTML = ''; // Clear previous content

    data.forEach(item => {
        const row = document.createElement('tr');
        
        // Determinamos si el stock es bajo para aplicar la clase CSS
        const stockClass = item.stock < LOW_STOCK_THRESHOLD ? 'low-stock' : '';

        row.innerHTML = `
            <td data-label="ID">${item.id}</td>
            <td data-label="Categoría">${item.category}</td>
            <td data-label="Modelo">${item.model}</td>
            <td data-label="Número de Serie" class="serial-col">${item.serial}</td>
            <td data-label="Ubicación" class="editable-location" contenteditable="true">${item.location}</td>
            <td data-label="Stock" class="${stockClass}">${item.stock}</td>
            <td data-label="Estado">${item.status}</td>
        `;
        tbody.appendChild(row);
    });
};

/**
 * Global Search Handler
 */
const handleSearch = (e) => {
    const query = e.target.value.toLowerCase();
    
    const filteredData = inventoryData.filter(item => {
        return (
            item.model.toLowerCase().includes(query) ||
            item.category.toLowerCase().includes(query) ||
            item.location.toLowerCase().includes(query)
        );
    });
    
    renderTable(filteredData);
};

// Event Listeners
document.getElementById('globalSearch').addEventListener('input', handleSearch);

// Initial Load
window.onload = () => {
    renderTable(inventoryData);
};