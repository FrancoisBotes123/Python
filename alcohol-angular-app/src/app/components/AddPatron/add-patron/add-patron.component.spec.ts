import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddPatronComponent } from './add-patron.component';

describe('AddPatronComponent', () => {
  let component: AddPatronComponent;
  let fixture: ComponentFixture<AddPatronComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AddPatronComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AddPatronComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
