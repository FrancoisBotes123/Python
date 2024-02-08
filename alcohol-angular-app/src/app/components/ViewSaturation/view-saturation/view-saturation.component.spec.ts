import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewSaturationComponent } from './view-saturation.component';

describe('ViewSaturationComponent', () => {
  let component: ViewSaturationComponent;
  let fixture: ComponentFixture<ViewSaturationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ViewSaturationComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ViewSaturationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
