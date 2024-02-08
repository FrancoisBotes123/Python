import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { ApiService } from '../../../services/api.service';
import { Patron } from '../../../interfaces/patron';

@Component({
  selector: 'app-add-patron',
  standalone: true,
  imports: [CommonModule, FormsModule,HttpClientModule],
  templateUrl: './add-patron.component.html',
  styleUrls: ['./add-patron.component.css']
})
export class AddPatronComponent {
  patrons: Patron[] = [];
  newPatron: Patron = { name: '', body_mass: 0 };
  isModalOpen = false;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.loadPatrons();
  }

  loadPatrons(): void {
    this.apiService.getPatrons().subscribe({
      next: (patrons) => {
        this.patrons = patrons;
      },
      error: (err) => {
        // Handle error
        console.error(err);
      }
    });
  }

  openModal(): void {
    this.isModalOpen = true;
  }

  closeModal(): void {
    this.isModalOpen = false;
  }

  addPatron(): void {
    this.apiService.addPatron(this.newPatron).subscribe({
      next: (patron) => {
        this.patrons.push(patron);
        this.newPatron = { name: '', body_mass: 0 }; // Reset for next input
        this.closeModal();
      },
      error: (err) => {
        // Handle error
        console.error(err);
      }
    });
  }
}
