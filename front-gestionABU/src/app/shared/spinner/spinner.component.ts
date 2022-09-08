import { SpinnerService } from './spinner.service';
import { Component, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-spinner',
  template: `
  <!-- Plantilla del spinner -->
  <div *ngIf="isLoading$ | async " class="overlay">
    <mat-spinner></mat-spinner>
  </div>
  `,
  styleUrls: ['./spinner.component.css']
})
export class SpinnerComponent implements OnDestroy {

  isLoading$ = this._spinnerSrv.isLoading$;

  constructor(private readonly _spinnerSrv: SpinnerService) { }

  ngOnDestroy(): void {
    this.isLoading$.unsubscribe();
  }



}
