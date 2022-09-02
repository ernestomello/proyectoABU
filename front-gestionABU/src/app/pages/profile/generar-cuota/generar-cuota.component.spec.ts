import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GenerarCuotaComponent } from './generar-cuota.component';

describe('GenerarCuotaComponent', () => {
  let component: GenerarCuotaComponent;
  let fixture: ComponentFixture<GenerarCuotaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GenerarCuotaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GenerarCuotaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
