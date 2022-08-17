import { Component, OnInit, EventEmitter, Input, Output } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import {MatSnackBar} from '@angular/material/snack-bar';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public datosLogin: FormGroup;
  hide = true;

  @Input() error: string | null;

  @Output() submitEM = new EventEmitter();

  constructor(
    private _fb: FormBuilder,
    private _snackBar: MatSnackBar
  ) {
    this.error = '';
    this.datosLogin = this._fb.group({
      email : new FormControl('', [Validators.required, Validators.email]),
      password: new FormControl('', [Validators.required]),
    });

  }

  ngOnInit(): void {

  }

  enviar() {
    if (this.datosLogin.invalid) {
      this.openSnackBar();
    }
    if (this.datosLogin.valid) {
      console.log(this.datosLogin.value);
    }
  }

  openSnackBar() {
    this._snackBar.open("Compruebe los campos", "OK", {
      duration: 5000
    });
  }

}
