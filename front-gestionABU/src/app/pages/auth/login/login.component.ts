import { Socio } from '@shared/models/socio.interface';
import { AuthService } from '@auth/auth.service';
import { Component, OnInit, EventEmitter, Input, Output, OnDestroy } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import {MatSnackBar} from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit, OnDestroy {

  private _subscription: Subscription = new Subscription();
  public datosLogin: FormGroup;
  hide = true;

  @Input() error: string | null;

  @Output() submitEM = new EventEmitter();

  constructor(
    private _fb: FormBuilder,
    private _snackBar: MatSnackBar,
    private _authSvc: AuthService,
    private _router:Router
  ) {
    // inizialiso las variables
    this.error = '';
    this.datosLogin = this._fb.group({
      email : new FormControl('', [Validators.required, Validators.email]),
      password: new FormControl('', [Validators.required]),
    });
  }

  ngOnInit(): void {  }

  ngOnDestroy(): void {
    this._subscription.unsubscribe(); //antes de eliminar el componente elimino la suscripcion
  }

  onLogin() {
    const formValue = this.datosLogin.value;
    // Si los campos no son validos lo advierto al usuario y no se envia informacion para el login
    if (this.datosLogin.invalid) {
      this.openSnackBar();
    }
    // Si los campos son validos se envia la informacion para hacer el login
    if (this.datosLogin.valid) {
      this._subscription.add(
        this._authSvc.login(formValue).subscribe(res => {
          if(res){
            this._router.navigate(['']);
          }
        })
      );
    }
  }

  openSnackBar() {
    this._snackBar.open("Compruebe los campos", "OK", {
      duration: 5000
    });
  }

}