# Flora-ERP

End-to-end Enterprise Resource Planning (ERP) system designed for floriculture and flower export operations—managing farm procurement, local & B2B sales, cold-chain international exports, real-time inventory, and workforce attendance tracking.

---

## Core Modules

### 1. Procurement & Farm Sourcing (Buying)
* Supplier and partner farm directory management.
* Purchase Order (PO) creation, intake grading (stem length, head size, variety), and Goods Received Notes (GRN).
* Automated reorder alerts for packaging materials, fertilizers, and cold-storage supplies.

### 2. Sales & Order Fulfillment (Selling)
* Local wholesale, auction, and direct B2B client order management.
* Dynamic pricing tiers by flower variety, grade, and stem count.
* Automated invoicing, payment tracking, and claim/credit note handling.

### 3. Cold-Chain Inventory & Packhouse
* Batch and lot tracking from harvest/intake to cold room storage.
* FIFO (First-In, First-Out) stock allocation to minimize vase-life loss.
* Real-time cold-room temperature logging and stock movement audit trails.

### 4. International Export & Logistics
* Generation of export documentation: **Commercial Invoices**, **Packing Lists**, **Airway Bill (AWB)** tracking, and **Phytosanitary Certificate** records.
* HS code mapping and destination customs compliance checklists.
* Shipment dispatch tracking from packhouse to airport freight forwarders.

### 5. Workforce & Shift Tracking (Workers)
* Digital clock-in and clock-out tracking for greenhouse, grading, and packhouse staff.
* Shift scheduling, overtime calculation, and productivity logging (e.g., bunches graded per shift).
* Role-Based Access Control (RBAC) for Farm Managers, Export Officers, Inventory Clerks, and HR.

---

## Suggested Tech Stack

* **Backend:** Python, Django, Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Task Queue & Alerts:** Celery + Redis (for low-stock, cold-chain, and shift-overtime notifications)
* **Authentication:** JWT (`djangorestframework-simplejwt`) with Role-Based Access Control
* **Containerization:** Docker & Docker Compose

---

## Getting Started

### Prerequisites
* Python 3.12+
* PostgreSQL 15+
* Redis (for background tasks and notifications)

### Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/VictorMwachi/flora-erp.git](https://github.com/VictorMwachi/flora-erp.git)
   cd flora-erp
