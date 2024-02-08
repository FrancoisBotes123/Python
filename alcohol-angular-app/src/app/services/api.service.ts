import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Patron } from '../interfaces/patron';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000'; // Update with your actual API URL

  constructor(private http: HttpClient) {}

  // Gets all patrons from the backend
  getPatrons(): Observable<Patron[]> {
    return this.http.get<Patron[]>(`${this.apiUrl}/patrons/`);
  }

  // Adds a new patron to the backend
  addPatron(patron: Patron): Observable<Patron> {
    return this.http.post<Patron>(`${this.apiUrl}/patrons/`, patron);
  }

  // Update an existing patron (assuming you have an endpoint for this)
  updatePatron(patron: Patron): Observable<Patron> {
    return this.http.put<Patron>(`${this.apiUrl}/patrons/${patron.id}`, patron);
  }

  // Delete a patron (assuming you have an endpoint for this)
  deletePatron(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/patrons/${id}`);
  }

  // Example of another method to get a single patron by ID
  getPatronById(id: number): Observable<Patron> {
    return this.http.get<Patron>(`${this.apiUrl}/patrons/${id}`);
  }

  // Add more methods as needed for other operations
}
