import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListCuotaComponent } from './list-cuota.component';

describe('ListCuotaComponent', () => {
  let component: ListCuotaComponent;
  let fixture: ComponentFixture<ListCuotaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListCuotaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListCuotaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
