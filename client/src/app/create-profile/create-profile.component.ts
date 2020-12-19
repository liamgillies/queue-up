import { Component, OnInit } from '@angular/core';
import { FormsModule, FormArray, FormControl, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
@Component({
  selector: 'app-create-profile',
  templateUrl: './create-profile.component.html',
  styleUrls: ['./create-profile.component.css']
})
export class CreateProfileComponent implements OnInit {

  LOL_RANKS = ['Challenger', 'Grandmasters', 'Master', 'Diamond I', 'Diamond II', 'Diamond III', 'Diamond IV', 
  'Platinum I', 'Platinum II', 'Platinum III', 'Platinum IV', 'Gold I', 'Gold II', 'Gold III', 'Gold IV', 
  'Silver I', 'Silver II', 'Silver III', 'Silver IV', 'Bronze I', 'Bronze II', 'Bronze III', 'Bronze IV', 
  'Iron I', 'Iron II', 'Iron III', 'Iron IV']

  LOL_ROLES = [
    { name: 'Top', value: 'top' },
    { name: 'Jungle', value: 'jungle' },
    { name: 'Middle', value: 'middle' },
    { name: 'Bottom', value: 'bottom' },
    { name: 'Support', value: 'support' },
]

  profileForm = new FormGroup({
    ign: new FormControl('', [Validators.required]),
    rank: new FormControl('', [Validators.required]),
    roles: new FormArray([], [Validators.required]),
    description: new FormControl('',[Validators.required, Validators.maxLength(100)]),
    opgg: new FormControl('', [Validators.required]),
    rolesLF: new FormArray([], [Validators.required]),
    lowRankLF: new FormControl('', [Validators.required]),
    highRankLF: new FormControl('', [Validators.required])
  });
  constructor() {}

  ngOnInit(): void {
  }

  changeRank(e) {
    this.profileForm.controls.rank.setValue(e.target.value, {
      onlySelf: true
    });
  }

  changeRankLow(e) {
    this.profileForm.controls.lowRankLF.setValue(e.target.value, {
      onlySelf: true
    });
  }

  changeRankHigh(e) {
    this.profileForm.controls.highRankLF.setValue(e.target.value, {
      onlySelf: true
    });
  }

  onCheckboxChange(e) {
    const checkArray: FormArray = this.profileForm.get('roles') as FormArray;
  
    if (e.target.checked) {
      checkArray.push(new FormControl(e.target.value));
    } else {
      let i: number = 0;
      checkArray.controls.forEach((item: FormControl) => {
        if (item.value == e.target.value) {
          checkArray.removeAt(i);
          return;
        }
        i++;
      });
    }
  }

  onCheckboxChangeLF(e) {
    const checkArray: FormArray = this.profileForm.get('rolesLF') as FormArray;
  
    if (e.target.checked) {
      checkArray.push(new FormControl(e.target.value));
    } else {
      let i: number = 0;
      checkArray.controls.forEach((item: FormControl) => {
        if (item.value == e.target.value) {
          checkArray.removeAt(i);
          return;
        }
        i++;
      });
    }
  }

  register() {
    console.log(this.profileForm.controls.ign.value);
  }
}
