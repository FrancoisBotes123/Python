import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecordConsumptionComponent } from './record-consumption.component';

describe('RecordConsumptionComponent', () => {
  let component: RecordConsumptionComponent;
  let fixture: ComponentFixture<RecordConsumptionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RecordConsumptionComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RecordConsumptionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
