import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:8000'; // Adjust if your API is hosted elsewhere

  constructor(private http: HttpClient) { }

  addPatron(patron: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/patrons/`, patron);
  }

  getPatrons(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/patrons/`);
  }

  addDrink(drink: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/drinks/`, drink);
  }

  recordConsumption(consumption: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/consumptions/`, consumption);
  }

  getPatronSaturation(patronId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/patrons/${patronId}/saturation/`);
  }
}
